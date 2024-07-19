import React, { useState } from 'react';
import { axiosInstance } from '../../../utils/api';
import { BudgetItem } from '../../../utils/interfaces';
import { BUDGET_TYPE, PURCHASE_TYPE } from '../../../utils/choices';
import Form from '../../components/common/Form';
import InputText from '../../components/common/inputs/InputText';
import InputTextArea from '../../components/common/inputs/InputTextArea';
import InputSelect from '../../components/common/inputs/InputSelect';
import InputNumber from '../../components/common/inputs/InputNumber';
import InputCheck from '../../components/common/inputs/InputCheck';

const BudgetItemPOST: React.FC = () => {
  const [form, setForm] = useState<BudgetItem>({
    number: '',
    cpc: '',
    description: '',
    activity: '',
    purchase_type: PURCHASE_TYPE[0].value,
    budget_type: BUDGET_TYPE[0].value,
    budget: '',
    c1: false,
    c2: false,
    c3: false,
  });

  const handleSubmit: React.FormEventHandler = (event: React.ChangeEvent) => {
    event.preventDefault();
    axiosInstance
      .post('/budget_item/', form)
      .then(response => {
        console.log(response.data);
        setForm({
          number: '',
          cpc: '',
          description: '',
          activity: '',
          purchase_type: PURCHASE_TYPE[0].value,
          budget_type: BUDGET_TYPE[0].value,
          budget: '',
          c1: false,
          c2: false,
          c3: false,
        });
      })
      .catch(error => {
        console.log(error);
      });
  };

  return (
    <Form
      handleSubmit={handleSubmit}
      header={'Registrar Nueva Partida Presupuestaria'}
    >
      <InputText
        label={'Número'}
        field={form.number}
        setField={event => setForm({ ...form, number: event.toUpperCase() })}
        maxLength={255}
      />
      <InputText
        label={'CPC'}
        field={form.cpc}
        setField={event => setForm({ ...form, cpc: event })}
        maxLength={15}
      />
      <InputTextArea
        label={'Descripción'}
        field={form.description}
        setField={event => setForm({ ...form, description: event.toUpperCase() })}
      />
      <InputTextArea
        label={'Actividad'}
        field={form.activity}
        setField={event => setForm({ ...form, activity: event.toUpperCase() })}
      />
      <InputSelect
        label={'Tipo de Compra'}
        field={form.purchase_type}
        setField={event => setForm({ ...form, purchase_type: event })}
        options={PURCHASE_TYPE}
      />
      <InputSelect
        label={'Tipo de Presupuesto'}
        field={form.budget_type}
        setField={event => setForm({ ...form, budget_type: event })}
        options={BUDGET_TYPE}
      />
      <InputNumber
        label={'Presupuesto'}
        field={form.budget}
        setField={event => setForm({ ...form, budget: event })}
        min={0}
      />
      <InputCheck
        label={'C1'}
        field={form.c1}
        setField={event => setForm({ ...form, c1: event })}
        required={false}
      />
      <InputCheck
        label={'C2'}
        field={form.c2}
        setField={event => setForm({ ...form, c2: event })}
        required={false}
      />
      <InputCheck
        label={'C3'}
        field={form.c3}
        setField={event => setForm({ ...form, c3: event })}
        required={false}
      />
    </Form>
  );
};

export default BudgetItemPOST;
