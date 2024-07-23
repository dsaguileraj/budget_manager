import { useParams } from "react-router-dom";

const BudgetItem: React.FC = () => {
  const params = useParams();
  return <h1>BudgetItem: {params.id}</h1>;
};

export default BudgetItem;
