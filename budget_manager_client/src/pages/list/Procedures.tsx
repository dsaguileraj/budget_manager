import { useEffect, useState } from 'react';
import { axiosInstance } from '../../../utils/api';
import Button from "../../components/common/Button";
import { Certification, Procedure } from '../../../utils/interfaces';

const Procedures = () => {
  const [certifications, setCertifications] = useState<Certification[]>([]);
  const [procedures, setProcedures] = useState<Procedure[]>([]);

  useEffect(() => {
    const axiosGET = async () => {
      const certification = await axiosInstance.get('/certification/');
      const procedure = await axiosInstance.get('/procedure/');
      const data = { certification: certification.data, procedure: procedure.data };
      setCertifications(data.certification);
      setProcedures(data.procedure);
    };
    axiosGET();
  }, []);

  const getCertifications = (id: number | undefined) => {
    let count = 0;
    certifications.forEach(certification => certification.procedure == id && count++);
    return count;
  };

  return (
    <>
      <h1>Procedimientos</h1>
      <table>
        <thead>
          <tr>
            <th>Procedimiento</th>
            <th>Régimen</th>
            <th>Tipo de Producto</th>
            <th>Tipo de Compra</th>
            <th>Certificaciones</th>
            <th colSpan={2}>Opciones</th>
          </tr>
        </thead>
        <tbody>
          {procedures.map((procedure, index) => (
            <tr key={index}>
              <th>{procedure.name}</th>
              <th>{procedure.regime}</th>
              <th>{procedure.product_type}</th>
              <th>{procedure.purchase_type}</th>
              <th>{getCertifications(procedure.id)}</th>
              <th><Button text={'Ver'}/></th>
              <th><Button text={'Eliminar'}/></th>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
};

export default Procedures;
