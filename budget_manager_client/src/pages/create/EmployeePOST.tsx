import React, { useState } from 'react';
import { axiosInstance } from '../../../utils/api';
import { Employee } from '../../../utils/interfaces';
import Form from '../../components/common/Form';
import InputText from '../../components/common/inputs/InputText';

const EmployeePOST: React.FC = () => {
  const [form, setForm] = useState<Employee>({
    ci: '',
    first_name: '',
    middle_name: '',
    first_last_name: '',
    middle_last_name: '',
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
          first_name: '',
          middle_name: '',
          first_last_name: '',
          middle_last_name: '',
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
      header={'Registrar Nuevo Contacto'}
    >
      <InputText
        label={'Cédula'}
        field={form.ci}
        setField={event => setForm({ ...form, ci: event })}
        maxLength={10}
      />
      <InputText
        label={'Primer Nombre'}
        field={form.first_name}
        setField={event => setForm({ ...form, first_name: event.toUpperCase() })}
        maxLength={50}
      />
      <InputText
        label={'Segundo Nombre'}
        field={form.middle_name}
        setField={event => setForm({ ...form, middle_name: event.toUpperCase() })}
        maxLength={50}
        required={false}
      />
      <InputText
        label={'Primer Apellido'}
        field={form.first_last_name}
        setField={event => setForm({ ...form, first_last_name: event.toUpperCase() })}
        maxLength={50}
      />
      <InputText
        label={'Segundo Apellido'}
        field={form.middle_last_name}
        setField={event => setForm({ ...form, middle_last_name: event.toUpperCase() })}
        maxLength={50}
        required={false}
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
