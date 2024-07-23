import { useParams } from "react-router-dom";

const Employee: React.FC = () => {
  const params = useParams();
  return <h1>Employee: {params.ci}</h1>;
};

export default Employee;
