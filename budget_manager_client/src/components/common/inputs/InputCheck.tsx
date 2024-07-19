interface Props {
  label: string;
  field: boolean;
  setField: (value: boolean) => void;
  required?: boolean;
  disabled?: boolean;
}

const InputCheck: React.FC<Props> = ({ label, field, setField, required = true, disabled = false }) => {
  const id: string = Math.random().toString();
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input
        type='number'
        id={id}
        value={field.toString()}
        onChange={event => setField(event.target.checked)}
        required={required}
        disabled={disabled}
      />
    </div>
  );
};

export default InputCheck;
