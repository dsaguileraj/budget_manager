import React, { useEffect, useState } from 'react';
import { axiosPOST, axiosInstance } from '../../../utils/api';
import { Department, Employee, Option } from '../../../utils/interfaces';
import Form from '../../components/common/Form';
import InputText from '../../components/common/inputs/InputText';
import InputSelect from '../../components/common/inputs/InputSelect';

const DepartmentPOST: React.FC = () => {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [form, setForm] = useState<Department>({
    name: '',
    director: employees[0]?.ci,
  });

  useEffect(() => {
    const axiosGET = async () => {
      const employee = await axiosInstance.get('employee/');
      setEmployees(employee.data);
      setForm({
        name: '',
        director: employee.data[0]?.ci,
      });
    };
    axiosGET();
  }, []);

  let employeesOptions: Option[] = [];
  employees.forEach(employee =>
    employeesOptions.push({
      value: employee.ci,
      label: `${employee.first_last_name} ${employee.middle_last_name} ${employee.middle_name} ${employee.first_name}`,
      disabled: false,
    })
  );

  const handleSubmit: React.FormEventHandler = (event: React.ChangeEvent) => {
    event.preventDefault();
    axiosPOST(
      'department/',
      form,
      setForm({
        name: '',
        director: employees[0]?.ci,
      })
    );
  };

  return (
    <Form
      handleSubmit={handleSubmit}
      header={'Registrar Nuevo Departmaneto'}
    >
      <InputText
        label={'Nombre'}
        field={form.name}
        setField={event => setForm({ ...form, name: event.toUpperCase() })}
        maxLength={50}
      />
      <InputSelect
        label={'Director'}
        field={form.director}
        setField={event => setForm({ ...form, director: event })}
        options={employeesOptions}
      />
    </Form>
  );
};

export default DepartmentPOST;
