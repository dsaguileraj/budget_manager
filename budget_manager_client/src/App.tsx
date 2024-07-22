import { BrowserRouter, Route, Routes } from 'react-router-dom';
// import { Navigation } from './components/Navigation.jsx';
import BudgetItemPOST from './pages/create/BudgetItemPOST';
import CertificationPOST from './pages/create/CertificationPOST';
import ContractPOST from './pages/create/ContractPOST';
import DepartmentPOST from './pages/create/DepartmentPOST';
import EmployeePOST from './pages/create/EmployeePOST';
import ProcedurePOST from './pages/create/ProcedurePOST';

function App() {
  return (
    <BrowserRouter>
      {/* <Navigation /> */}
      <Routes>
        <Route path='/budget_item/create' element={<BudgetItemPOST />}/>
        <Route path='/certification/create' element={<CertificationPOST />}/>
        <Route path='/contract/create' element={<ContractPOST />}/>
        <Route path='/department/create' element={<DepartmentPOST />}/>
        <Route path='/employee/create' element={<EmployeePOST />}/>
        <Route path='/procedure/create' element={<ProcedurePOST />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
