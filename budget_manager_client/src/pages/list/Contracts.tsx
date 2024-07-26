import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { axiosInstance } from '../../../utils/api';
import Button from '../../components/common/Button';
import { Certification, Contract, Employee } from '../../../utils/interfaces';

const Contracts: React.FC = () => {
  const [certifications, setCertifications] = useState<Certification[]>([]);
  const [contracts, setContracts] = useState<Contract[]>([]);
  const [employees, setEmployees] = useState<Employee[]>([]);

  useEffect(() => {
    const axiosGET = async () => {
      const certification = await axiosInstance.get('certification/');
      const contract = await axiosInstance.get('contract/');
      const employee = await axiosInstance.get('employee/');
      const data = { certification: certification.data, contract: contract.data, employee: employee.data };
      setCertifications(data.certification);
      setContracts(data.contract);
      setEmployees(data.employee);
    };
    axiosGET();
  }, []);

  const navigate = useNavigate();

  const getAdmin = (id: string | number | undefined) => {
    const index = employees.findIndex(employee => employee.ci == id);
    return `${employees[index].first_last_name} ${employees[index].middle_last_name} ${employees[index].first_name} ${employees[index].middle_name}`;
  };

  const getBudget = (id: string | number | undefined) => {
    const index = certifications.findIndex(certification => certification.id == id);
    return certifications[index].budget;
  };

  const getCertification = (id: string | number | undefined) => {
    const index = certifications.findIndex(certification => certification.id == id);
    return certifications[index].number;
  };

  const getDescription = (id: string | number | undefined) => {
    const index = certifications.findIndex(certification => certification.id == id);
    return certifications[index].description;
  };

  return (
    <>
      <h1>Contratos</h1>
      <table>
        <thead>
          <tr>
            <th>Número</th>
            <th>Certificación</th>
            <th>Descripción</th>
            <th>Administrador</th>
            <th>Contratista</th>
            <th>Presupesto</th>
            <th colSpan={2}>Opciones</th>
          </tr>
        </thead>
        <tbody>
          {contracts.map((contract, index) => (
            <tr key={index}>
              <th>{contract.number}</th>
              <th>{getCertification(contract.certification)}</th>
              <th>{getDescription(contract.certification)}</th>
              <th>{getAdmin(contract.admin)}</th>
              <th>{contract.contractor}</th>
              <th>{getBudget(contract.certification)}</th>
              <th>
                <Button
                  text={'Ver'}
                  onClick={() => navigate(`/contract/${contract.id}/`)}
                />
              </th>
              <th>
                <Button
                  text={'Eliminar'}
                  onClick={async () => {
                    try {
                      const confirm = window.confirm('¿Está seguro de que desea eliminar?');
                      confirm && (await axiosInstance.delete(`/contract/${contract.id}/`));
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

export default Contracts;
