import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { axiosGET } from '../../../utils/api';
import { Contract, Employee } from '../../../utils/interfaces';

const EmployeeDetail: React.FC = () => {
  const [contracts, setConctracts] = useState<Contract[]>([]);
  const [employee, setEmployee] = useState<Employee | null>(null);
  const params = useParams();

  const getContract = (id: string | number | undefined) => {
    let query: Contract[] = [];
    contracts.forEach(contract => contract.id == id && query.push(contract));
    return query;
  };

  useEffect(() => {
    axiosGET('contract/', setConctracts);
    axiosGET(`employee/${params.ci}/`, setEmployee);
    setConctracts(getContract(params.ci));
  }, []);

  return (
    <>
      <p>Param: {params.ci}</p>
      <p>ID: {employee?.ci}</p>
      <p>Nombres: {employee?.first_name} {employee?.middle_name}</p>
      <p>Apellidos: {employee?.first_last_name} {employee?.middle_last_name}</p>
      <p>Correo: {employee?.email}</p>
      <p>Usuario: {employee?.user}</p>
      <ol>
        {contracts.map((contract, index) => (
          <li key={index}>{contract.number}</li>
        ))}
      </ol>
    </>
  );
};

export default EmployeeDetail;
