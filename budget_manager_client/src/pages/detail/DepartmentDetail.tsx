import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { axiosGET } from '../../../utils/api';
import { Certification, Department, Employee } from '../../../utils/interfaces';

const DepartmentDetail: React.FC = () => {
  const [certifications, setCertifications] = useState<Certification[]>([]);
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [department, setDepartment] = useState<Department | null>(null);
  const params = useParams();

  const getCertification = (id: string | number | undefined) => {
    let cert: Certification[] = [];
    certifications.forEach(certification => certification.id == id && cert.push(certification));
    return cert;
  };

  const getDirector = (id: string | number | undefined) => {
    const index = employees.findIndex(employee => employee?.ci == id);
    return `${employees[index]?.first_last_name} ${employees[index]?.middle_last_name} ${employees[index]?.first_name} ${employees[index]?.middle_name}`;
  };

  useEffect(() => {
    axiosGET('certification/', setCertifications);
    axiosGET('employee/', setEmployees);
    axiosGET(`department/${params.id}/`, setDepartment);
    setCertifications(getCertification(params.id));
  }, []);

  return (
    <>
      <p>Param: {params.id}</p>
      <p>ID: {department?.id}</p>
      <p>Nombre: {department?.name}</p>
      <p>Director: {getDirector(department?.director)}</p>
      <ol>
        {certifications.map((certification, index) => (
          <li key={index}>{certification.number}</li>
        ))}
      </ol>
    </>
  );
};

export default DepartmentDetail;
