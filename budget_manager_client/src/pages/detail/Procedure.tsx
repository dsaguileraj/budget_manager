import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { axiosGET, axiosInstance } from '../../../utils/api';
import { Procedure } from '../../../utils/interfaces';

const ProcedureDetail: React.FC = () => {
  const [procedure, setProcedure] = useState<Procedure | null>(null);
  const params = useParams();

  useEffect(() => {
    axiosGET(`/procedure/4/`, setProcedure);
  }, []);

  return (
    <>
      <p>Param: {params.id}</p>
      <p>ID: {procedure?.id}</p>
      <p>Nombre: {procedure?.name}</p>
      <p>Régimen: {procedure?.regime}</p>
      <p>Tipo de Producto: {procedure?.product_type}</p>
      <p>Tipo de Compra: {procedure?.purchase_type}</p>
    </>
  );
};

export default ProcedureDetail;
