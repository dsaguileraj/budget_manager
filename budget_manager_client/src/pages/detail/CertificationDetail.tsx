import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { axiosGET } from '../../../utils/api';
import { Certification } from '../../../utils/interfaces';

const CertificationDetail: React.FC = () => {
  const [certification, setCertification] = useState<Certification | null>(null);
  const params = useParams();

  useEffect(() => {
    axiosGET(`certification/${params.id}/`, setCertification);
  }, []);

  return (
    <>
      <p>Param: {params.id}</p>
      <p>Presupuesto: USD {certification?.budget}</p>
      <p>Partida: {certification?.budget_item}</p>
      <p>Departamento: {certification?.department}</p>
      <p>Descripcion: {certification?.description}</p>
      <p>ID: {certification?.id}</p>
      <p>No.: {certification?.number}</p>
      <p>Procedimiento: {certification?.procedure}</p>
    </>
  );
};

export default CertificationDetail;
