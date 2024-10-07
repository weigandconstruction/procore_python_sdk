# DependentImportParams

Dependent Import Params Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** | Names of all Managed Equipment categories specified for Managed Equipment dependent import | [optional] 
**types** | **List[str]** | Names of all Managed Equipment types specified for Managed Equipment dependent import | [optional] 

## Example

```python
from procore_sdk.models.dependent_import_params import DependentImportParams

# TODO update the JSON string below
json = "{}"
# create an instance of DependentImportParams from a JSON string
dependent_import_params_instance = DependentImportParams.from_json(json)
# print the JSON string representation of the object
print(DependentImportParams.to_json())

# convert the object into a dict
dependent_import_params_dict = dependent_import_params_instance.to_dict()
# create an instance of DependentImportParams from a dict
dependent_import_params_from_dict = DependentImportParams.from_dict(dependent_import_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


