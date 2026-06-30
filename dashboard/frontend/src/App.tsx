import { Navigate, Route, Routes } from 'react-router-dom'
import { AppShell } from './components/layout/AppShell'
import { AboutPage } from './pages/AboutPage'
import { CheckpointsPage } from './pages/CheckpointsPage'
import { CloudPage } from './pages/CloudPage'
import { DashboardPage } from './pages/DashboardPage'
import { DatasetsPage } from './pages/DatasetsPage'
import { ExperimentsPage } from './pages/ExperimentsPage'
import { LogsPage } from './pages/LogsPage'
import { ModelsPage } from './pages/ModelsPage'
import { SettingsPage } from './pages/SettingsPage'
import { TrainingPage } from './pages/TrainingPage'

function App() {
  return (
    <Routes>
      <Route element={<AppShell />}>
        <Route index element={<DashboardPage />} />
        <Route path="training" element={<TrainingPage />} />
        <Route path="models" element={<ModelsPage />} />
        <Route path="datasets" element={<DatasetsPage />} />
        <Route path="experiments" element={<ExperimentsPage />} />
        <Route path="checkpoints" element={<CheckpointsPage />} />
        <Route path="cloud" element={<CloudPage />} />
        <Route path="settings" element={<SettingsPage />} />
        <Route path="logs" element={<LogsPage />} />
        <Route path="about" element={<AboutPage />} />
        <Route path="*" element={<Navigate replace to="/" />} />
      </Route>
    </Routes>
  )
}

export default App
