export interface BudgetItem {
  id?: number;
  number: string;
  cpc: string;
  description: string;
  activity: string;
  purchase_type: string | number | undefined;
  budget_type: string | number | undefined;
  budget: number | string;
  c1: boolean;
  c2: boolean;
  c3: boolean;
}

export interface Certification {
  id?: number;
  number: string;
  department: string | number | undefined;
  budget_item: string | number | undefined;
  procedure: string | number | undefined;
  description: string;
  budget: string | number;
}

export interface Contract {
  id?: number;
  number: string;
  certification: string | number | undefined;
  admin: string | number | undefined;
  contractor: string;
  duration: number;
  date: Date;
}

export interface Department {
  id?: number;
  name: string;
  director: string | number | undefined;
}

export interface Employee {
  ci: string;
  first_name: string;
  middle_name: string;
  first_last_name: string;
  middle_last_name: string;
  email: string;
  user: string;
}

export interface Option {
  value: string | number | undefined;
  label: string;
  disabled?: boolean;
}

export interface Procedure {
  id?: number;
  name: string;
  regime: string | number | undefined;
  product_type: string | number | undefined;
  purchase_type: string | number | undefined;
}
