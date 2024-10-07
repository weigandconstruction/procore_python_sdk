# Body100


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Unique identifier for the company. | 
**standard_cost_code_list** | [**StandardCostCodeList1**](StandardCostCodeList1.md) |  | 

## Example

```python
from procore_sdk.models.body100 import Body100

# TODO update the JSON string below
json = "{}"
# create an instance of Body100 from a JSON string
body100_instance = Body100.from_json(json)
# print the JSON string representation of the object
print(Body100.to_json())

# convert the object into a dict
body100_dict = body100_instance.to_dict()
# create an instance of Body100 from a dict
body100_from_dict = Body100.from_dict(body100_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


