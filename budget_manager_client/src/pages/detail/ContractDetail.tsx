import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { axiosGET } from '../../../utils/api';
import { Certification, Contract, Employee } from '../../../utils/interfaces';

const ContractDetail: React.FC = () => {
  const [certifications, setCertifications] = useState<Certification[]>([]);
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [contract, setContract] = useState<Contract | null>(null);
  const params = useParams();

  const getCertifications = (id: string | number | undefined) => {
    let cert: Certification[] = [];
    certifications.forEach(certification => certification.id == id && cert.push(certification));
    return cert;
  };

  const getCertification = (id: string | number | undefined) => {
    const index = certifications.findIndex(certification => certification?.id == id);
    return certifications[index]?.number
  };

  const getAdmin = (id: string | number | undefined) => {
    const index = employees.findIndex(employee => employee?.ci == id);
    return `${employees[index]?.first_last_name} ${employees[index]?.middle_last_name} ${employees[index]?.first_name} ${employees[index]?.middle_name}`;
  };

  useEffect(() => {
    axiosGET('certification/', setCertifications);
    axiosGET('employee/', setEmployees);
    axiosGET(`contract/${params.id}/`, setContract);
    setCertifications(getCertifications(params.id));
  }, []);

  return (
    <>
      <p>Param: {params.id}</p>
      <p>Número: {contract?.number}</p>
      <p>Certificacion: {getCertification(contract?.certification)}</p>
      <p>Administrador: {getAdmin(contract?.admin)}</p>
      <p>Contratista: {contract?.contractor}</p>
      <p>Fecha: {contract?.date.toDateString()}</p>
      <p>Plazo: {contract?.duration}</p>
    </>
  );
};

export default ContractDetail;
