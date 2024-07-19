import React, { useEffect, useState } from 'react';
import { axiosInstance } from '../../../utils/api';
import { AdminHistory, Contract, Employee, Option } from '../../../utils/interfaces';
import Form from '../../components/common/Form';
import InputSelect from '../../components/common/inputs/InputSelect';

const AdminHistoryPOST: React.FC = () => {
  const [contracts, setContracts] = useState<Contract[]>([]);
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [form, setForm] = useState<AdminHistory>({
    contract: 1,
    admin: 1,
  });

  useEffect(() => {
    const axiosGET = async () => {
      const contract = await axiosInstance.get('/contract/');
      const employee = await axiosInstance.get('/employee/');
      const data = { contract: contract.data, employee: employee.data };
      setContracts(data.contract);
      setEmployees(data.employee);
    };
    axiosGET();
  }, []);

  let contractsOptions: Option[] = [];
  contracts.forEach(contract =>
    contractsOptions.push({
      value: contract.id,
      label: contract.number,
      disabled: false,
    })
  );

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
    axiosInstance
      .post('/contract/history/', form)
      .then(response => {
        console.log(response.data);
        setForm({
          contract: 1,
          admin: 1,
        });
      })
      .catch(error => {
        console.log(error);
      });
  };

  return (
    <Form
      handleSubmit={handleSubmit}
      header={'Registrar Nuevo Administrador'}
    >
      <InputSelect
        label={'Contrato'}
        field={form.contract}
        setField={event => setForm({ ...form, contract: event })}
        options={employeesOptions}
      />
      <InputSelect
        label={'Administrador'}
        field={form.admin}
        setField={event => setForm({ ...form, admin: event })}
        options={contractsOptions}
      />
    </Form>
  );
};

export default AdminHistoryPOST;
