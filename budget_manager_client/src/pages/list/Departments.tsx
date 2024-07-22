import { useEffect, useState } from 'react';
import { axiosInstance } from '../../../utils/api';
import Button from "../../components/common/Button";
import { Certification, Department, Employee } from '../../../utils/interfaces';

const Departments = () => {
  const [certifications, setCertifications] = useState<Certification[]>([]);
  const [departments, setDepartments] = useState<Department[]>([]);
  const [employees, setEmployees] = useState<Employee[]>([]);

  useEffect(() => {
    const axiosGET = async () => {
      const certification = await axiosInstance.get('/certification/');
      const department = await axiosInstance.get('/department/');
      const employee = await axiosInstance.get('/employee/');
      const data = { certification: certification.data, department: department.data, employee: employee.data };
      setCertifications(data.certification);
      setDepartments(data.department);
      setEmployees(data.employee);
    };
    axiosGET();
  }, []);

  const getCertifications = (id: number | undefined) => {
    let count = 0;
    certifications.forEach(certification => certification.procedure == id && count++);
    return count;
  };

  const getDirector = (id: string | number |undefined) => {
    const index = employees.findIndex(employee => employee.ci == id)
    return `${employees[index].first_last_name} ${employees[index].middle_last_name} ${employees[index].first_name} ${employees[index].middle_name}`
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
              <th><Button text={'Ver'}/></th>
              <th><Button text={'Eliminar'}/></th>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
};

export default Departments;
