import Button from './Button';

interface Props {
  handleSubmit: React.FormEventHandler<HTMLFormElement>;
  header: string;
  children: React.ReactNode;
}

const Form: React.FC<Props> = ({ handleSubmit, header, children }) => {
  return (
    <form onSubmit={handleSubmit}>
      <h1>{header}</h1>
      {children}
      <Button />
      <Button text={'Cancelar'}/>
    </form>
  );
};

export default Form;
