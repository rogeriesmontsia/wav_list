
import React from 'react';
import { Discover } from '../pages'
const DashboardLayout = ({ children }) => {
  return (
    <div>
  <header className="sticky top-0"><Discover /></header>
      {children}
    </div>
  );
}

export default DashboardLayout;
