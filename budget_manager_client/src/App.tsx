import { BrowserRouter, Route, Routes } from 'react-router-dom';
// import { Navigation } from './components/Navigation.jsx';
import BudgetItemPOST from './pages/create/BudgetItemPOST';
import BudgetItems from './pages/list/BudgetItems';
import BudgetItem from './pages/detail/BudgetItem';
import CertificationPOST from './pages/create/CertificationPOST';
import Certifications from './pages/list/Certifications';
import Certification from './pages/detail/Certification';
import ContractPOST from './pages/create/ContractPOST';
import Contracts from './pages/list/Contracts';
import Contract from './pages/detail/Contract';
import DepartmentPOST from './pages/create/DepartmentPOST';
import Departments from './pages/list/Departments';
import Department from './pages/detail/Department';
import EmployeePOST from './pages/create/EmployeePOST';
import Employees from './pages/list/Employees';
import Employee from './pages/detail/Employee';
import ProcedurePOST from './pages/create/ProcedurePOST';
import Procedures from './pages/list/Procedures';
import Procedure from './pages/detail/Procedure';

function App() {
  return (
    <BrowserRouter>
      {/* <Navigation /> */}
      <Routes>
        <Route path='/budget_item/create' element={<BudgetItemPOST />}/>
        <Route path='/budget_item/:id' element={<BudgetItem />}/>
        <Route path='/budget_item/' element={<BudgetItems />}/>
        <Route path='/certification/create' element={<CertificationPOST />}/>
        <Route path='/certification/:id' element={<Certification />}/>
        <Route path='/certification/' element={<Certifications />}/>
        <Route path='/contract/create' element={<ContractPOST />}/>
        <Route path='/contract/:id' element={<Contract />}/>
        <Route path='/contract/' element={<Contracts />}/>
        <Route path='/department/create' element={<DepartmentPOST />}/>
        <Route path='/department/:id' element={<Department />}/>
        <Route path='/department/' element={<Departments />}/>
        <Route path='/employee/create' element={<EmployeePOST />}/>
        <Route path='/employee/:ci' element={<Employee />}/>
        <Route path='/employee/' element={<Employees />}/>
        <Route path='/procedure/create' element={<ProcedurePOST />}/>
        <Route path='/procedure/:id' element={<Procedure />}/>
        <Route path='/procedure/' element={<Procedures />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
