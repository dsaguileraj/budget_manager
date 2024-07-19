import React, { useEffect, useState } from 'react';
import { axiosInstance } from '../../../utils/api';
import { Certification, Contract, Option } from '../../../utils/interfaces';
import Form from '../../components/common/Form';
import InputText from '../../components/common/inputs/InputText';
import InputSelect from '../../components/common/inputs/InputSelect';
import InputNumber from '../../components/common/inputs/InputNumber';
import InputDate from '../../components/common/inputs/InputDate';

const ContractPOST: React.FC = () => {
  const [certifications, setCertifications] = useState<Certification[]>([]);
  const [form, setForm] = useState<Contract>({
    number: '',
    certification: 1,
    contractor: '',
    duration: 0,
    date: new Date(),
  });

  useEffect(() => {
    const axiosGET = async () => {
      const response = await axiosInstance.get('/certification/');
      const data = response.data;
      setCertifications(data);
    };
    axiosGET();
  }, []);

  let certOptions: Option[] = [];
  certifications.forEach(certification => {
    certOptions.push({
      value: certification.id,
      label: `${certification.number} - ${certification.budget_item}`,
      disabled: false,
    });
  });

  const handleSubmit: React.FormEventHandler = (event: React.ChangeEvent) => {
    event.preventDefault();
    axiosInstance
      .post('/contract/', form)
      .then(response => {
        console.log(response.data);
        setForm({
          number: '',
          certification: 1,
          contractor: '',
          duration: 0,
          date: new Date(),
        });
      })
      .catch(error => {
        console.log(error);
      });
  };

  return (
    <Form
      handleSubmit={handleSubmit}
      header={'Registrar Nuevo Contrato'}
    >
      <InputText
        label={'Número'}
        field={form.number}
        setField={event => setForm({ ...form, number: event.toUpperCase() })}
        maxLength={25}
      />
      <InputSelect
        label={'Certificación'}
        field={form.certification}
        setField={event => setForm({ ...form, certification: event })}
        options={certOptions}
      />
      <InputText
        label={'Contratista'}
        field={form.contractor}
        setField={event => setForm({ ...form, contractor: event.toUpperCase() })}
        maxLength={100}
      />
      <InputNumber
        label={'Plazo'}
        field={form.duration}
        setField={event => setForm({ ...form, duration: event })}
        min={0}
      />
      <InputDate
        label={'Suscripción de Contrato'}
        field={form.date}
        setField={event => setForm({ ...form, date: event })}
      />
    </Form>
  );
};

export default ContractPOST;
