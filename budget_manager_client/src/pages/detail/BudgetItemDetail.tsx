import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { axiosGET } from '../../../utils/api';
import { BudgetItem } from '../../../utils/interfaces';

const BudgetItemDetail: React.FC = () => {
  const [budgetItem, setBudgetItem] = useState<BudgetItem | null>(null);
  const params = useParams();

  useEffect(() => {
    axiosGET(`budget_ttem/${params.id}/`, setBudgetItem);
  }, []);

  return (
    <>
      <p>Param: {params.id}</p>
      <p>Actividad: {budgetItem?.activity}</p>
      <p>Presupuesto: {budgetItem?.budget}</p>
      <p>Tipo de Presupuesto: {budgetItem?.budget_type}</p>
      <p>C1: {budgetItem?.c1}</p>
      <p>C2: {budgetItem?.c2}</p>
      <p>C3: {budgetItem?.c3}</p>
      <p>CPC: {budgetItem?.cpc}</p>
      <p>Descripcion: {budgetItem?.description}</p>
      <p>ID: {budgetItem?.id}</p>
      <p>No.: {budgetItem?.number}</p>
      <p>Tipo de Compra: {budgetItem?.purchase_type}</p>
    </>
  );
};

export default BudgetItemDetail;
