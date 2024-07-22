import { useEffect, useState } from 'react';
import { axiosInstance } from '../../../utils/api';
import Button from "../../components/common/Button";
import { Contract, Employee } from '../../../utils/interfaces';

const Employees = () => {
  const [contracts, setContracts] = useState<Contract[]>([]);
  const [employees, setEmployees] = useState<Employee[]>([]);

  useEffect(() => {
    const axiosGET = async () => {
      const contract = await axiosInstance.get('/contract/');
      const employee = await axiosInstance.get('/employee/');
      const data = { contract: contract.data, employee: employee.data };
      setContracts(data.contract);
      setEmployees(data.employee);
    };
    axiosGET();
  }, []);

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
              <th>{employee.first_last_name} {employee.middle_last_name} {employee.first_name} {employee.middle_name}</th>
              <th>{employee.email}</th>
              <th>{employee.user}</th>
              <th>{getContracts(employee.ci)}</th>
              <th><Button text={'Ver'}/></th>
              <th><Button text={'Eliminar'}/></th>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
};

export default Employees;
