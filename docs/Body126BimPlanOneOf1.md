# Body126BimPlanOneOf1

BIM Plan

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
from procore_sdk.models.body126_bim_plan_one_of1 import Body126BimPlanOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of Body126BimPlanOneOf1 from a JSON string
body126_bim_plan_one_of1_instance = Body126BimPlanOneOf1.from_json(json)
# print the JSON string representation of the object
print(Body126BimPlanOneOf1.to_json())

# convert the object into a dict
body126_bim_plan_one_of1_dict = body126_bim_plan_one_of1_instance.to_dict()
# create an instance of Body126BimPlanOneOf1 from a dict
body126_bim_plan_one_of1_from_dict = Body126BimPlanOneOf1.from_dict(body126_bim_plan_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


