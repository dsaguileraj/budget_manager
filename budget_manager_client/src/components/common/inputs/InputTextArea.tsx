interface Props {
  label: string;
  field: string;
  setField: (value: string) => void;
  required?: boolean;
  disabled?: boolean;
}

const InputTextArea: React.FC<Props> = ({ label, field, setField, required = true, disabled = false }) => {
  return (
    <div>
      <label htmlFor={field}>{label}</label>
      <textarea
        id={field}
        value={field}
        onChange={event => setField(event.target.value)}
        required={required}
        disabled={disabled}
      ></textarea>
    </div>
  );
};

export default InputTextArea;
