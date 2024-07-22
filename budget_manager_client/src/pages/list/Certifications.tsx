import { useEffect, useState } from 'react';
import { axiosInstance } from '../../../utils/api';
import Button from '../../components/common/Button';
import { BudgetItem, Certification } from '../../../utils/interfaces';

const Certifications = () => {
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

  const getBudgetItem = (id: string | number |undefined) => {
    const index = budgetItems.findIndex(budgetItem => budgetItem.id == id)
    return budgetItems[index].number
  };

  const getActivity = (id: string | number |undefined) => {
    const index = budgetItems.findIndex(budgetItem => budgetItem.id == id)
    return budgetItems[index].activity
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
                <Button text={'Ver'} />
              </th>
              <th>
                <Button text={'Eliminar'} />
              </th>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
};

export default Certifications;
