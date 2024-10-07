# Body126BimPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_level_id** | **int** | ID of the BIM Level to be associated to the plan | 
**sheet_map_start** | [**RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart**](RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart.md) |  | [optional] 
**sheet_map_end** | [**RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart**](RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart.md) |  | [optional] 
**model_map_start** | [**RestV10BimPlansGet200ResponseInnerAllOfModelMapStart**](RestV10BimPlansGet200ResponseInnerAllOfModelMapStart.md) |  | [optional] 
**model_map_end** | [**RestV10BimPlansGet200ResponseInnerAllOfModelMapStart**](RestV10BimPlansGet200ResponseInnerAllOfModelMapStart.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body126_bim_plan import Body126BimPlan

# TODO update the JSON string below
json = "{}"
# create an instance of Body126BimPlan from a JSON string
body126_bim_plan_instance = Body126BimPlan.from_json(json)
# print the JSON string representation of the object
print(Body126BimPlan.to_json())

# convert the object into a dict
body126_bim_plan_dict = body126_bim_plan_instance.to_dict()
# create an instance of Body126BimPlan from a dict
body126_bim_plan_from_dict = Body126BimPlan.from_dict(body126_bim_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


