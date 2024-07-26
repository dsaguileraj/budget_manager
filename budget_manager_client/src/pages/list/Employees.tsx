import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { axiosInstance } from '../../../utils/api';
import Button from '../../components/common/Button';
import { Contract, Employee } from '../../../utils/interfaces';

const Employees: React.FC = () => {
  const [contracts, setContracts] = useState<Contract[]>([]);
  const [employees, setEmployees] = useState<Employee[]>([]);

  useEffect(() => {
    const axiosGET = async () => {
      const contract = await axiosInstance.get('contract/');
      const employee = await axiosInstance.get('employee/');
      const data = { contract: contract.data, employee: employee.data };
      setContracts(data.contract);
      setEmployees(data.employee);
    };
    axiosGET();
  }, []);

  const navigate = useNavigate();

  const getContracts = (id: string | undefined) => {
    let count = 0;
    contracts.forEach(contract => contract.admin == id && count++);
    return count;
  };

  return (
    <>
      <h1>Empleados</h1>
      <table>
        <thead>
          <tr>
            <th>Cédula</th>
            <th>Empleado</th>
            <th>Correo</th>
            <th>Usuario</th>
            <th>Contratos</th>
            <th colSpan={2}>Opciones</th>
          </tr>
        </thead>
        <tbody>
          {employees.map((employee, index) => (
            <tr key={index}>
              <th>{employee.ci}</th>
              <th>
                {employee.first_last_name} {employee.middle_last_name} {employee.first_name} {employee.middle_name}
              </th>
              <th>{employee.email}</th>
              <th>{employee.user}</th>
              <th>{getContracts(employee.ci)}</th>
              <th>
                <Button
                  text={'Ver'}
                  onClick={() => navigate(`/employee/${employee.ci}/`)}
                />
              </th>
              <th>
                <Button
                  text={'Eliminar'}
                  onClick={async () => {
                    try {
                      const confirm = window.confirm('¿Está seguro de que desea eliminar?');
                      confirm && (await axiosInstance.delete(`/employee/${employee.ci}/`));
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

export default Employees;
