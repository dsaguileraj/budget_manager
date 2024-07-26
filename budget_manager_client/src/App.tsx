import { BrowserRouter, Route, Routes } from 'react-router-dom';
// import { Navigation } from './components/Navigation.jsx';
import BudgetItemPOST from './pages/create/BudgetItemPOST';
import BudgetItems from './pages/list/BudgetItems';
import BudgetItemDetail from './pages/detail/BudgetItemDetail';
import CertificationPOST from './pages/create/CertificationPOST';
import Certifications from './pages/list/Certifications';
import CertificationDetail from './pages/detail/CertificationDetail';
import ContractPOST from './pages/create/ContractPOST';
import Contracts from './pages/list/Contracts';
import ContractDetail from './pages/detail/ContractDetail';
import DepartmentPOST from './pages/create/DepartmentPOST';
import Departments from './pages/list/Departments';
import DepartmentDetail from './pages/detail/DepartmentDetail';
import EmployeePOST from './pages/create/EmployeePOST';
import Employees from './pages/list/Employees';
import EmployeeDetail from './pages/detail/EmployeeDetail';
import ProcedurePOST from './pages/create/ProcedurePOST';
import Procedures from './pages/list/Procedures';
import ProcedureDetail from './pages/detail/ProcedureDetail';

function App() {
  return (
    <BrowserRouter>
      {/* <Navigation /> */}
      <Routes>
        <Route path='/budget_item/create' element={<BudgetItemPOST />}/>
        <Route path='/budget_item/:id' element={<BudgetItemDetail />}/>
        <Route path='/budget_item/' element={<BudgetItems />}/>
        <Route path='/certification/create' element={<CertificationPOST />}/>
        <Route path='/certification/:id' element={<CertificationDetail />}/>
        <Route path='/certification/' element={<Certifications />}/>
        <Route path='/contract/create' element={<ContractPOST />}/>
        <Route path='/contract/:id' element={<ContractDetail />}/>
        <Route path='/contract/' element={<Contracts />}/>
        <Route path='/department/create' element={<DepartmentPOST />}/>
        <Route path='/department/:id' element={<DepartmentDetail />}/>
        <Route path='/department/' element={<Departments />}/>
        <Route path='/employee/create' element={<EmployeePOST />}/>
        <Route path='/employee/:ci' element={<EmployeeDetail />}/>
        <Route path='/employee/' element={<Employees />}/>
        <Route path='/procedure/create' element={<ProcedurePOST />}/>
        <Route path='/procedure/:id' element={<ProcedureDetail />}/>
        <Route path='/procedure/' element={<Procedures />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
