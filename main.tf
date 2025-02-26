provider "azurerm" {
  features {}
  subscription_id = "yoursubcriptionid"
  tenant_id = "yourusername.onmicrosoft.com"
}

resource "azurerm_resource_group" "rg" {
  name     = "iot-project-rg" //change for your rg name
  location = "northeurope" //change your location
}

//example names
resource "azurerm_kubernetes_cluster" "aks" {
  name                = "iot-aks-cluster" 
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "iotcluster"

  default_node_pool {
    name       = "default"
    node_count = 2
    vm_size    = "Standard_DS2_v2"
  }

  identity {
    type = "SystemAssigned"
  }
}
