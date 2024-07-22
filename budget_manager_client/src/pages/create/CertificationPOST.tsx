import React, { useEffect, useState } from 'react';
import { axiosInstance } from '../../../utils/api';
import { BudgetItem, Certification, Department, Option, Procedure } from '../../../utils/interfaces';
import Form from '../../components/common/Form';
import InputNumber from '../../components/common/inputs/InputNumber';
import InputSelect from '../../components/common/inputs/InputSelect';
import InputText from '../../components/common/inputs/InputText';
import InputTextArea from '../../components/common/inputs/InputTextArea';

const CertificationPOST: React.FC = () => {
  const [budgetItems, setBudgetItems] = useState<BudgetItem[]>([]);
  const [departments, setDepartments] = useState<Department[]>([]);
  const [procedures, setProcedures] = useState<Procedure[]>([]);
  const [form, setForm] = useState<Certification>({
    number: '',
    department: departments[0]?.id,
    budget_item: budgetItems[0]?.id,
    procedure: procedures[0]?.id,
    description: '',
    budget: '',
  });

  useEffect(() => {
    const axiosGET = async () => {
      const budgetItem = await axiosInstance.get('/budget_item/');
      const department = await axiosInstance.get('/department/');
      const procedure = await axiosInstance.get('/procedure/');
      const data = { budgetItem: budgetItem.data, department: department.data, procedure: procedure.data };
      setBudgetItems(data.budgetItem);
      setDepartments(data.department);
      setProcedures(data.procedure);
      setForm({
        number: '',
        department: data.department[0].id,
        budget_item: data.budgetItem[0].id,
        procedure: data.procedure[0].id,
        description: '',
        budget: '',
      });
    };
    axiosGET();
  }, []);

  let budgetItemsOptions: Option[] = [];
  budgetItems.forEach(budgetItem => {
    budgetItemsOptions.push({
      value: budgetItem.id,
      label: `${budgetItem.number} - ${budgetItem.activity}`,
      disabled: false,
    });
  });

  let departmentsOptions: Option[] = [];
  departments.forEach(department => {
    departmentsOptions.push({
      value: department.id,
      label: department.name,
      disabled: false,
    });
  });

  let proceduressOptions: Option[] = [];
  procedures.forEach(procedure => {
    proceduressOptions.push({
      value: procedure.id,
      label: `${procedure.name} (${procedure.purchase_type})`,
      disabled: false,
    });
  });

  const handleSubmit: React.FormEventHandler = (event: React.ChangeEvent) => {
    event.preventDefault();
    axiosInstance
      .post('/certification/', form)
      .then(response => {
        console.log(response.data);
        setForm({
          number: '',
          department: departments[0]?.id,
          budget_item: budgetItems[0]?.id,
          procedure: procedures[0]?.id,
          description: '',
          budget: '',
        });
      })
      .catch(error => {
        console.log(error);
      });
  };

  return (
    <Form
      handleSubmit={handleSubmit}
      header={'Registrar Nueva Certificación'}
    >
      <InputText
        label={'Número'}
        field={form.number}
        setField={event => setForm({ ...form, number: event.toUpperCase() })}
        maxLength={25}
      />
      <InputSelect
        label={'Departamento'}
        field={form.department}
        setField={event => setForm({ ...form, department: event })}
        options={departmentsOptions}
      />
      <InputSelect
        label={'Partida Presupuestaria'}
        field={form.budget_item}
        setField={event => setForm({ ...form, budget_item: event })}
        options={budgetItemsOptions}
      />
      <InputSelect
        label={'Procedimiento'}
        field={form.procedure}
        setField={event => setForm({ ...form, procedure: event })}
        options={proceduressOptions}
      />
      <InputTextArea
        label={'Descripción'}
        field={form.description}
        setField={event => setForm({ ...form, description: event.toUpperCase() })}
      />
      <InputNumber
        label={'Presupuesto Referencial'}
        field={form.budget}
        setField={event => setForm({ ...form, budget: event })}
        min={0}
      />
    </Form>
  );
};

export default CertificationPOST;
