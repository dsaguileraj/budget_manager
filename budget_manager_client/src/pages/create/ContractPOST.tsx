import React, { useEffect, useState } from 'react';
import { axiosPOST, axiosInstance } from '../../../utils/api';
import { Certification, Contract, Employee, Option } from '../../../utils/interfaces';
import Form from '../../components/common/Form';
import InputText from '../../components/common/inputs/InputText';
import InputSelect from '../../components/common/inputs/InputSelect';
import InputNumber from '../../components/common/inputs/InputNumber';
import InputDate from '../../components/common/inputs/InputDate';

const ContractPOST: React.FC = () => {
  const [certifications, setCertifications] = useState<Certification[]>([]);
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [form, setForm] = useState<Contract>({
    number: '',
    certification: certifications[0]?.id,
    admin: employees[0]?.ci,
    contractor: '',
    duration: 0,
    date: new Date(),
  });

  useEffect(() => {
    const axiosGET = async () => {
      const certification = await axiosInstance.get('certification/');
      const employee = await axiosInstance.get('employee/');
      setCertifications(certification.data);
      setEmployees(employee.data);
      setForm({
        number: '',
        certification: certification.data[0]?.id,
        admin: employee.data[0]?.ci,
        contractor: '',
        duration: 0,
        date: new Date(),
      });
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

  let employeesOptions: Option[] = [];
  employees.forEach(employee => {
    employeesOptions.push({
      value: employee.ci,
      label: `${employee.first_last_name} ${employee.middle_last_name} ${employee.first_name} ${employee.middle_name} (${employee.ci})`,
      disabled: false,
    });
  });

  const handleSubmit: React.FormEventHandler = (event: React.ChangeEvent) => {
    event.preventDefault();
    axiosPOST(
      'contract/',
      form,
      setForm({
        number: '',
        certification: certifications[0]?.id,
        admin: employees[0]?.ci,
        contractor: '',
        duration: 0,
        date: new Date(),
      })
    );
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
      <InputSelect
        label={'Administrador'}
        field={form.admin}
        setField={event => setForm({ ...form, admin: event })}
        options={employeesOptions}
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
