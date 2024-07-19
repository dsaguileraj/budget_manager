export interface AdminHistory {
  contract: string;
  admin: string;
  resolution: File | undefined;
}

export interface BudgetItem {
  number: string;
  cpc: string;
  description: string;
  activity: string;
  purchase_type: string;
  budget_type: string;
  budget: number;
  c1: boolean;
  c2: boolean;
  c3: boolean;
}

export interface Certification {
  number: string;
  department: number;
  budget_item: number;
  procedure: number;
  description: string;
  reference_budget: number;
  awarded_budget: number;
  certification: File | undefined;
  resolution: File | undefined;
}

export interface Contract {
  number: string;
  certification: number;
  contractor: string;
  duration: number;
  date: Date;
  contract: File | undefined;
}

export interface Department {
  name: string;
  director: string | number | undefined;
}

export interface Employee {
  ci: string;
  name: string;
  last_name: string;
  email: string;
  user: string;
}

export interface Option {
  value: string | number | undefined;
  label: string;
}

export interface Procedure {
  name: string;
  regime: string | number | undefined;
  product_type: string | number | undefined;
  purchase_type: string | number | undefined;
}
