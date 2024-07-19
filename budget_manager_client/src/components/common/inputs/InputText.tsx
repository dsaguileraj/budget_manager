interface Props {
  label: string;
  field: string;
  setField: (value: string) => void;
  maxLength?: number;
  required?: boolean;
  disabled?: boolean;
}

const InputText: React.FC<Props> = ({ label, field, setField, maxLength = 255, required = true, disabled = false }) => {
  const id: string = Math.random().toString();
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input
        type='text'
        id={id}
        value={field}
        onChange={event => setField(event.target.value)}
        maxLength={maxLength}
        required={required}
        disabled={disabled}
      />
    </div>
  );
};

export default InputText;
