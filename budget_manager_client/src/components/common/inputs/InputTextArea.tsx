interface Props {
  label: string;
  field: string;
  setField: (value: string) => void;
  required?: boolean;
  disabled?: boolean;
}

const InputTextArea: React.FC<Props> = ({ label, field, setField, required = true, disabled = false }) => {
  const id: string = Math.random().toString();
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <textarea
        id={id}
        value={field}
        onChange={event => setField(event.target.value)}
        required={required}
        disabled={disabled}
      ></textarea>
    </div>
  );
};

export default InputTextArea;
