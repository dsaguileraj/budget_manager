import React, { useEffect, useState } from 'react';
import { axiosInstance } from '../../../utils/api';
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
      const response = await axiosInstance.get('/employee/');
      const data = response.data;
      setEmployees(data);
    };
    axiosGET();
  }, []);

  let employeesOptions: Option[] = [{ value: undefined, label: '---', disabled: true }];
  employees.forEach(employee =>
    employeesOptions.push({
      value: employee.ci,
      label: `${employee.first_last_name} ${employee.middle_last_name} ${employee.middle_name} ${employee.first_name}`,
      disabled: false,
    })
  );

  const handleSubmit: React.FormEventHandler = (event: React.ChangeEvent) => {
    event.preventDefault();
    axiosInstance
      .post('/department/', form)
      .then(response => {
        console.log(response.data);
        setForm({
          name: '',
          director: employees[0]?.ci,
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
