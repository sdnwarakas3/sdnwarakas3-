create table if not exists public.app_state (
  school_code text primary key,
  classes jsonb not null default '{}'::jsonb,
  school_setting jsonb not null default '{}'::jsonb,
  version bigint not null default 0,
  updated_at timestamptz not null default now()
);

alter table public.app_state enable row level security;
