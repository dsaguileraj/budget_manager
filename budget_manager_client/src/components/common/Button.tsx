interface ButtonProps {
  text?: String;
  onClick?: () => void;
}

const Button: React.FC<ButtonProps> = ({ text = 'Guardar', onClick }) => {
  return <button onClick={onClick}>{text}</button>;
};

export default Button;
