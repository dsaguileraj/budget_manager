import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { axiosInstance } from '../../../utils/api';
import Button from '../../components/common/Button';
import { BudgetItem, Certification } from '../../../utils/interfaces';

const Certifications: React.FC = () => {
  const [certifications, setCertifications] = useState<Certification[]>([]);
  const [budgetItems, setBudgetItems] = useState<BudgetItem[]>([]);

  useEffect(() => {
    const axiosGET = async () => {
      const budgetItem = await axiosInstance.get('/budget_item/');
      const certification = await axiosInstance.get('/certification/');
      const data = { budgetItem: budgetItem.data, certification: certification.data };
      setBudgetItems(data.budgetItem);
      setCertifications(data.certification);
    };
    axiosGET();
  }, []);

  const navigate = useNavigate();

  const getBudgetItem = (id: string | number | undefined) => {
    const index = budgetItems.findIndex(budgetItem => budgetItem.id == id);
    return budgetItems[index].number;
  };

  const getActivity = (id: string | number | undefined) => {
    const index = budgetItems.findIndex(budgetItem => budgetItem.id == id);
    return budgetItems[index].activity;
  };

  return (
    <>
      <h1>Certificaciones</h1>
      <table>
        <thead>
          <tr>
            <th>Número</th>
            <th>Partida</th>
            <th>Descripción</th>
            <th>Actividad</th>
            <th>Presupesto</th>
            <th colSpan={2}>Opciones</th>
          </tr>
        </thead>
        <tbody>
          {certifications.map((certification, index) => (
            <tr key={index}>
              <th>{certification.number}</th>
              <th>{getBudgetItem(certification.budget_item)}</th>
              <th>{certification.description}</th>
              <th>{getActivity(certification.budget_item)}</th>
              <th>USD {certification.budget}</th>
              <th>
                <Button
                  text={'Ver'}
                  onClick={() => navigate(`/certification/${certification.id}/`)}
                />
              </th>
              <th>
                <Button
                  text={'Eliminar'}
                  onClick={async () => {
                    try {
                      const confirm = window.confirm('¿Está seguro de que desea eliminar?');
                      confirm && (await axiosInstance.delete(`/certification/${certification.id}/`));
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

export default Certifications;
