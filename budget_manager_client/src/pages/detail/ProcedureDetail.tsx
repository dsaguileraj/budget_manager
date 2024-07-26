import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { axiosGET } from '../../../utils/api';
import { Certification, Procedure } from '../../../utils/interfaces';

const ProcedureDetail: React.FC = () => {
  const [certifications, setCertifications] = useState<Certification[]>([]);
  const [procedure, setProcedure] = useState<Procedure | null>(null);
  const params = useParams();

  const getCertifications = (id: string | number | undefined) => {
    let query: Certification[] = [];
    certifications.forEach(certification => certification.id == id && query.push(certification));
    return query;
  };

  useEffect(() => {
    axiosGET('certification/', setCertifications);
    axiosGET(`procedure/${params.id}/`, setProcedure);
    setCertifications(getCertifications(params.id));
  }, []);

  return (
    <>
      <p>Param: {params.id}</p>
      <p>ID: {procedure?.id}</p>
      <p>Nombre: {procedure?.name}</p>
      <p>Régimen: {procedure?.regime}</p>
      <p>Tipo de Producto: {procedure?.product_type}</p>
      <p>Tipo de Compra: {procedure?.purchase_type}</p>
      <ol>
        {certifications.map((certification, index) => (
          <li key={index}>{certification.number}</li>
        ))}
      </ol>
    </>
  );
};

export default ProcedureDetail;
