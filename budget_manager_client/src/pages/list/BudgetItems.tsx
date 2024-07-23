import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { axiosInstance } from '../../../utils/api';
import Button from '../../components/common/Button';
import { BudgetItem } from '../../../utils/interfaces';

const BudgetItems: React.FC = () => {
  const [budgetItems, setBudgetItems] = useState<BudgetItem[]>([]);

  useEffect(() => {
    const axiosGET = async () => {
      const response = await axiosInstance.get('/budget_item/');
      const data = response.data;
      setBudgetItems(data);
    };
    axiosGET();
  }, []);

  const navigate = useNavigate();

  return (
    <>
      <h1>Partidas Presupuestarias</h1>
      <table>
        <thead>
          <tr>
            <th>Partida</th>
            <th>CPC</th>
            <th>Descripción</th>
            <th>Actividad</th>
            <th>C1</th>
            <th>C2</th>
            <th>C3</th>
            <th>Presupesto</th>
            <th colSpan={2}>Opciones</th>
          </tr>
        </thead>
        <tbody>
          {budgetItems.map((budgetItem, index) => (
            <tr key={index}>
              <th>{budgetItem.number}</th>
              <th>{budgetItem.cpc}</th>
              <th>{budgetItem.description}</th>
              <th>{budgetItem.activity}</th>
              <th>{budgetItem.c1 && 'X'}</th>
              <th>{budgetItem.c2 && 'X'}</th>
              <th>{budgetItem.c3 && 'X'}</th>
              <th>USD {budgetItem.budget}</th>
              <th>
                <Button
                  text={'Ver'}
                  onClick={() => navigate(`/budget_item/${budgetItem.id}/`)}
                />
              </th>
              <th>
                <Button
                  text={'Eliminar'}
                  onClick={async () => {
                    try {
                      const confirm = window.confirm('¿Está seguro de que desea eliminar?');
                      confirm && (await axiosInstance.delete(`/budget_item/${budgetItem.id}/`));
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

export default BudgetItems;
