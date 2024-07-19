import React, { useState } from 'react';
import { axiosInstance } from '../../../utils/api';
import { Employee } from '../../../utils/interfaces';
import Form from '../../components/common/Form';
import InputText from '../../components/common/inputs/InputText';

const EmployeePOST: React.FC = () => {
  const [form, setForm] = useState<Employee>({
    ci: '',
    name: '',
    last_name: '',
    email: '',
    user: '',
  });

  const handleSubmit: React.FormEventHandler = (event: React.ChangeEvent) => {
    event.preventDefault();
    axiosInstance
      .post('/employee/', form)
      .then(response => {
        console.log(response.data);
        setForm({
          ci: '',
          name: '',
          last_name: '',
          email: '',
          user: '',
        });
      })
      .catch(error => {
        console.log(error);
      });
  };

  return (
    <Form
      handleSubmit={handleSubmit}
      header={'Registrar Nuevo Procedimiento'}
    >
      <InputText
        label={'Cédula'}
        field={form.ci}
        setField={event => setForm({ ...form, ci: event })}
        maxLength={10}
      />
      <InputText
        label={'Nombres'}
        field={form.name}
        setField={event => setForm({ ...form, name: event })}
        maxLength={50}
      />
      <InputText
        label={'Apellidos'}
        field={form.last_name}
        setField={event => setForm({ ...form, last_name: event })}
        maxLength={50}
      />
      <InputText
        label={'Correo'}
        field={form.email}
        setField={event => setForm({ ...form, email: event })}
        maxLength={100}
      />
      <InputText
        label={'Usuario'}
        field={form.user}
        setField={event => setForm({ ...form, user: event })}
        maxLength={50}
      />
    </Form>
  );
};

export default EmployeePOST;
