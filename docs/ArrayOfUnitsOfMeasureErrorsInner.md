# ArrayOfUnitsOfMeasureErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**is_standard** | **bool** | Unit of Measure is among the standard units provided by Procore by default | [optional] 
**name** | **str** | Name of Unit of Measure | [optional] 
**description** | **str** | Description of Unit of Measure | [optional] 
**uom_category** | [**RestV10CompaniesCompanyIdUomsGet200ResponseInnerUomCategory**](RestV10CompaniesCompanyIdUomsGet200ResponseInnerUomCategory.md) |  | [optional] 
**errors** | [**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_units_of_measure_errors_inner import ArrayOfUnitsOfMeasureErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUnitsOfMeasureErrorsInner from a JSON string
array_of_units_of_measure_errors_inner_instance = ArrayOfUnitsOfMeasureErrorsInner.from_json(json)
# print the JSON string representation of the object
print(ArrayOfUnitsOfMeasureErrorsInner.to_json())

# convert the object into a dict
array_of_units_of_measure_errors_inner_dict = array_of_units_of_measure_errors_inner_instance.to_dict()
# create an instance of ArrayOfUnitsOfMeasureErrorsInner from a dict
array_of_units_of_measure_errors_inner_from_dict = ArrayOfUnitsOfMeasureErrorsInner.from_dict(array_of_units_of_measure_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


