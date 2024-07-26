import React, { useState } from 'react';
import { axiosPOST } from '../../../utils/api';
import { Procedure } from '../../../utils/interfaces';
import { PRODUCT_TYPE, PURCHASE_TYPE, REGIME_TYPE } from '../../../utils/choices';
import Form from '../../components/common/Form';
import InputSelect from '../../components/common/inputs/InputSelect';
import InputText from '../../components/common/inputs/InputText';

const ProcedurePOST: React.FC = () => {
  const [form, setForm] = useState<Procedure>({
    name: '',
    regime: REGIME_TYPE[0].value,
    product_type: PRODUCT_TYPE[0].value,
    purchase_type: PURCHASE_TYPE[0].value,
  });

  const handleSubmit: React.FormEventHandler = (event: React.ChangeEvent) => {
    event.preventDefault();
    axiosPOST(
      'procedure/',
      form,
      setForm({
        name: '',
        regime: REGIME_TYPE[0].value,
        product_type: PRODUCT_TYPE[0].value,
        purchase_type: PURCHASE_TYPE[0].value,
      })
    );
  };

  return (
    <Form
      handleSubmit={handleSubmit}
      header={'Registrar Nuevo Procedimiento'}
    >
      <InputText
        label={'Nombre'}
        field={form.name}
        setField={event => setForm({ ...form, name: event.toUpperCase() })}
        maxLength={50}
      />
      <InputSelect
        label={'Régimen'}
        field={form.regime}
        setField={event => setForm({ ...form, regime: event })}
        options={REGIME_TYPE}
        required={false}
      />
      <InputSelect
        label={'Tipo de Producto'}
        field={form.product_type}
        setField={event => setForm({ ...form, product_type: event })}
        options={PRODUCT_TYPE}
        required={false}
      />
      <InputSelect
        label={'Tipo de Compra'}
        field={form.purchase_type}
        setField={event => setForm({ ...form, purchase_type: event })}
        options={PURCHASE_TYPE}
      />
    </Form>
  );
};

export default ProcedurePOST;
