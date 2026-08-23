-- Tidak wajib dijalankan manual. server.js membuat tabel otomatis.
CREATE TABLE IF NOT EXISTS school_state (
  school_code TEXT PRIMARY KEY,
  classes JSONB NOT NULL DEFAULT '{}'::jsonb,
  school_setting JSONB NOT NULL DEFAULT '{"nama":"SD NEGERI WARAKAS 3","tahun":"2026/2027"}'::jsonb,
  version BIGINT NOT NULL DEFAULT 0,
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS sync_log (
  id BIGSERIAL PRIMARY KEY,
  school_code TEXT NOT NULL,
  client_id TEXT,
  version BIGINT NOT NULL,
  changed_at BIGINT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
