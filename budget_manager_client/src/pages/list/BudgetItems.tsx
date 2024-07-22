import { useEffect, useState } from 'react';
import { axiosInstance } from '../../../utils/api';
import Button from "../../components/common/Button";
import { BudgetItem } from '../../../utils/interfaces';

const BudgetItems = () => {
  const [budgetItems, setBudgetItems] = useState<BudgetItem[]>([]);

  useEffect(() => {
    const axiosGET = async () => {
      const response = await axiosInstance.get('/budget_item/');
      const data = response.data;
      setBudgetItems(data);
    };
    axiosGET();
  }, []);

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
              <th><Button text={'Ver'}/></th>
              <th><Button text={'Eliminar'}/></th>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
};

export default BudgetItems;
