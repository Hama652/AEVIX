export interface HealthResponse {
  service: string
  status: string
  environment: string
}

export interface DashboardStatusResponse {
  application: string
  environment: string
  authentication_enabled: boolean
  current_user: {
    subject: string
    display_name: string
    authenticated: boolean
  }
  websocket_connections: number
  training_status: string
  experiments: string
}

export interface ApiClient {
  baseUrl: string
}

export const apiClient: ApiClient = {
  baseUrl: import.meta.env.VITE_AEVIX_DASHBOARD_API_URL ?? 'http://127.0.0.1:8000',
}
