import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { axiosInstance } from '../../../utils/api';
import Button from '../../components/common/Button';
import { Certification, Department, Employee } from '../../../utils/interfaces';

const Departments: React.FC = () => {
  const [certifications, setCertifications] = useState<Certification[]>([]);
  const [departments, setDepartments] = useState<Department[]>([]);
  const [employees, setEmployees] = useState<Employee[]>([]);

  useEffect(() => {
    const axiosGET = async () => {
      const certification = await axiosInstance.get('certification/');
      const department = await axiosInstance.get('department/');
      const employee = await axiosInstance.get('employee/');
      setCertifications(certification.data);
      setDepartments(department.data);
      setEmployees(employee.data);      
    };
    axiosGET();
  }, []);

  const navigate = useNavigate();

  const getCertifications = (id: number | undefined) => {
    let count = 0;
    certifications.forEach(certification => certification.procedure == id && count++);
    return count;
  };

  const getDirector = (id: string | number | undefined) => {
    const index = employees.findIndex(employee => employee?.ci == id);
    return `${employees[index]?.first_last_name} ${employees[index]?.middle_last_name} ${employees[index]?.first_name} ${employees[index]?.middle_name}`;
  };

  return (
    <>
      <h1>Departamentos</h1>
      <table>
        <thead>
          <tr>
            <th>Departamento</th>
            <th>Director</th>
            <th>Certificaciones</th>
            <th colSpan={2}>Opciones</th>
          </tr>
        </thead>
        <tbody>
          {departments.map((department, index) => (
            <tr key={index}>
              <th>{department.name}</th>
              <th>{getDirector(department.director)}</th>
              <th>{getCertifications(department.id)}</th>
              <th>
                <Button
                  text={'Ver'}
                  onClick={() => navigate(`/department/${department.id}/`)}
                />
              </th>
              <th>
                <Button
                  text={'Eliminar'}
                  onClick={async () => {
                    try {
                      const confirm = window.confirm('¿Está seguro de que desea eliminar?');
                      confirm && (await axiosInstance.delete(`/department/${department.id}/`));
                      confirm && window.location.reload();
                    } catch (error) {
                      if (error == 'AxiosError: Request failed with status code 500') {
                        alert(
                          'No se pudo eliminar la instancia debido a que se hace referencia a ella a través de claves externas protegidas. Primero elimine las instancias hijas que lo referencian.'
                        );
                      }
                    }
                  }}
                />
              </th>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
};

export default Departments;
