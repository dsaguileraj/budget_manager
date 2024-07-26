import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { axiosInstance } from '../../../utils/api';
import Button from '../../components/common/Button';
import { Certification, Procedure } from '../../../utils/interfaces';

const Procedures: React.FC = () => {
  const [certifications, setCertifications] = useState<Certification[]>([]);
  const [procedures, setProcedures] = useState<Procedure[]>([]);

  useEffect(() => {
    const axiosGET = async () => {
      const certification = await axiosInstance.get('certification/');
      const procedure = await axiosInstance.get('procedure/');
      const data = { certification: certification.data, procedure: procedure.data };
      setCertifications(data.certification);
      setProcedures(data.procedure);
    };
    axiosGET();
  }, []);

  const navigate = useNavigate();

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
              <th>
                <Button
                  text={'Ver'}
                  onClick={() => navigate(`/procedure/${procedure.id}/`)}
                />
              </th>
              <th>
                <Button
                  text={'Eliminar'}
                  onClick={async () => {
                    try {
                      const confirm = window.confirm('¿Está seguro de que desea eliminar?');
                      confirm && (await axiosInstance.delete(`/procedure/${procedure.id}/`));
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

export default Procedures;
