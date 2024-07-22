import { BrowserRouter, Route, Routes } from 'react-router-dom';
// import { Navigation } from './components/Navigation.jsx';
import BudgetItemPOST from './pages/create/BudgetItemPOST';
import BudgetItems from './pages/list/BudgetItems';
import CertificationPOST from './pages/create/CertificationPOST';
import Certifications from './pages/list/Certifications';
import ContractPOST from './pages/create/ContractPOST';
import Contracts from './pages/list/Contracts';
import DepartmentPOST from './pages/create/DepartmentPOST';
import Departments from './pages/list/Departments';
import EmployeePOST from './pages/create/EmployeePOST';
import Employees from './pages/list/Employees';
import ProcedurePOST from './pages/create/ProcedurePOST';
import Procedures from './pages/list/Procedures';

function App() {
  return (
    <BrowserRouter>
      {/* <Navigation /> */}
      <Routes>
        <Route path='/budget_item/create' element={<BudgetItemPOST />}/>
        <Route path='/budget_item/' element={<BudgetItems />}/>
        <Route path='/certification/create' element={<CertificationPOST />}/>
        <Route path='/certification/' element={<Certifications />}/>
        <Route path='/contract/create' element={<ContractPOST />}/>
        <Route path='/contract/' element={<Contracts />}/>
        <Route path='/department/create' element={<DepartmentPOST />}/>
        <Route path='/department/' element={<Departments />}/>
        <Route path='/employee/create' element={<EmployeePOST />}/>
        <Route path='/employee/' element={<Employees />}/>
        <Route path='/procedure/create' element={<ProcedurePOST />}/>
        <Route path='/procedure/' element={<Procedures />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
