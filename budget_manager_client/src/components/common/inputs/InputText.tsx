interface Props {
  label: string;
  field: string;
  setField: (value: string) => void;
  maxLength?: number;
  required?: boolean;
  disabled?: boolean;
}

const InputText: React.FC<Props> = ({
  label,
  field,
  setField,
  maxLength = 255,
  required = true,
  disabled = false
}) => {
  return (
    <div>
      <label htmlFor={field}>{label}</label>
      <input
        type='text'
        id={field}
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
